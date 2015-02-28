'use strict';

/**
 * @ngdoc function
 * @name srcFeApp.controller:MainCtrl
 * @description
 * # MainCtrl
 * Controller of the srcFeApp
 */
angular.module('srcFeApp')
  .controller('MainCtrl', function ($scope) {
    $scope.awesomeThings = [
      'HTML5 Boilerplate',
      'AngularJS',
      'Karma'
    ];
  });
