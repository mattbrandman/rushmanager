(function() {

    var rushApp = angular.module('routerApp', ['ui.router', 'RushApp', 'commentApp', 'eventManagement']);

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
            .state('events', {
                abstract: true,
                url: "/events",
                template: "<div ui-view></div>"
            })
            .state('events.list', {
                url: "/list",
                templateUrl: "static/events/event_list.html",
                controller: "EventController as ctrl"
            })
            .state('events.detail', {
                url: "/:id",
                templateUrl: "static/events/event_detail.html",
                controller: "EventDetailController as ctrl",
                resolve: {
                    promiseObj: function($http, $stateParams) {
                        return $http.get('/api/events/' + $stateParams.id);
                    }
                }
            })
            .state('events.attendance', {
                url: "/attendance/:id",
                templateUrl: "static/events/take_attendance.html",
                controller: "EventAttendanceController as ctrl"
            })
    });
})();
