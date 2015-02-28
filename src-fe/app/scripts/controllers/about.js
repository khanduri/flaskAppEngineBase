'use strict';

/**
 * @ngdoc function
 * @name srcFeApp.controller:AboutCtrl
 * @description
 * # AboutCtrl
 * Controller of the srcFeApp
 */
angular.module('srcFeApp')
  .controller('AboutCtrl', function ($scope) {
    $scope.awesomeThings = [
      'HTML5 Boilerplate',
      'AngularJS',
      'Karma'
    ];
  });
