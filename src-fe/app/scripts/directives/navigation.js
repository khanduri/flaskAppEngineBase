'use strict';

/**
 * @ngdoc directive
 * @name srcFeApp.directive:navigation
 * @description
 * # navigation
 */

angular.module('srcFeApp')
    .directive('customnavigation', function (Login, $location) {
        return {
            templateUrl: 'views/templates/navigation.html',
            restrict: 'E',
            controller: function(){

                this.isLoggedIn = Login.isAuthenticated();

                this.tabIndex = null;

                this.setSelected = function(tabIndex){
                    this.tabIndex = tabIndex;
                };

                this.isSelected = function(tabIndex){
                    return this.tabIndex === tabIndex;
                }

                this.logout = function(){
                    Login.logout(function(){
                        $location.path('/');
                    });
                };
            },
            controllerAs: 'navigationCtrl'
        };
    });
