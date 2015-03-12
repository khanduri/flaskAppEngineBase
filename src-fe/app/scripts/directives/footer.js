'use strict';

/**
 * @ngdoc directive
 * @name srcFeApp.directive:footer
 * @description
 * # footer
 */
angular.module('srcFeApp')
  .directive('customfooter', function () {
    return {
      templateUrl: 'views/templates/footer.html',
      restrict: 'E',
      controller: function(){

      },
      controllerAs: 'footerCtrl'
    };
  });
