'use strict';

/**
 * @ngdoc function
 * @name srcFeApp.controller:LoginCtrl
 * @description
 * # LoginCtrl
 * Controller of the srcFeApp
 */
angular.module('srcFeApp')
    .controller('LoginCtrl', function ($scope, Login, $localStorage, $location) {
        $scope.login = function(){
            var form = {
                email: $scope.email,
                password: $scope.password
            };

            Login.login(form, function(response){
                if (response.meta.status == 200) {
                    $localStorage.token = response.data.token;
                    $location.path('/');
                }
            }, function(){
                console.log("some error");
            });
        };

        $scope.logout = function(){
            Login.logout(function(){
                $location.path('/');
            });
        };

        $scope.register = function (){

        };

        $scope.authenticate = function(){

        };
    });
