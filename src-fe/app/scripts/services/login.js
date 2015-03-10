'use strict';

/**
 * @ngdoc service
 * @name srcFeApp.login
 * @description
 * # login
 * Service in the srcFeApp.
 */
angular.module('srcFeApp')
    .service('Login', function Login($http, $localStorage) {
        var baseUrl = "http://localhost:8080/api/users";

        function urlBase64Decode(str) {
            var output = str.replace('-', '+').replace('_', '/');
            switch (output.length % 4) {
                case 0:
                    break;
                case 2:
                    output += '==';
                    break;
                case 3:
                    output += '=';
                    break;
                default:
                    throw 'Illegal base64url string!';
            }
            return window.atob(output);
        }

        function getUserFromToken() {
            var token = $localStorage.token;
            var user = {};
            if (typeof token !== 'undefined') {
                var encoded = token.split('.')[1];
                user = JSON.parse(urlBase64Decode(encoded));
            }
            return user;
        }

        var currentUser = getUserFromToken();

        function changeUser(user) {
            currentUser = user;
        }

        return {
            register: function(data, success, error) {
                $http.post(baseUrl + '/register', data).success(success).error(error)
            },
            login: function(data, success, error) {
                $http.post(baseUrl + '/login', data).success(success).error(error)
            },
            authenticate: function(success, error) {
                $http.get(baseUrl + '/me').success(success).error(error)
            },
            logout: function(success) {
                changeUser(undefined);
                delete $localStorage.token;
                success();
            },
            isAuthenticated: function(){
                if (currentUser == undefined){
                    return false;
                }
                if (Object.keys(currentUser).length === 0){
                    return false;
                }
                return true;
            }
        };
    });

