(function() {

var rushApp = angular.module('routerApp', ['ui.router', 'RushApp', 'commentApp']);

rushApp.config(function($stateProvider, $urlRouterProvider) {
  //
  // For any unmatched url, redirect to /state1
  $urlRouterProvider.otherwise("/rush/list");
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
      controller: 'RushTableController as ctrl'
    })
    .state('rush.detail', {
      url: "/:id",
      templateUrl: "static/comments/comment_list.html",

    })
});
})();