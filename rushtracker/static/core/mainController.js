(function() {

var rushApp = angular.module('routerApp', ['ui.router', 'RushApp', 'commentApp']);

rushApp.config(function($stateProvider, $urlRouterProvider, $locationProvider) {
  //
  // For any unmatched url, redirect to /state1
  $urlRouterProvider.otherwise("/rush/list");
  $locationProvider.html5Mode(false);
  //
  // Now set up the states
  $stateProvider
    .state('rush', {
      abstract: true,
      url: "/rush",
      template: "<div ui-view></div>"
    })
    .state('rush.list', {
      url: "/list",
      templateUrl: "static/rushtracker/index.html",
      controller: 'RushTableController as ctrl',
      resolve: {
        promiseObj: function($http) {
          return $http.get('/api/rush/');
        },
        brotherPromiseObj: function($http) {
          return $http.get('/api/users/');
        }
      }
    })
    .state('rush.detail', {
      url: "/:id",
      templateUrl: "static/comments/comment_list.html",

    })
});
})();