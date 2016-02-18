(function() {

    var rushApp = angular.module('routerApp', ['ui.router', 'RushApp', 'commentApp', 'eventManagement', 'chapterManagement', 'recruitmentPeriod', 'ngMaterial', 'md.data.table', '720kb.datepicker']);

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
                template: "<div layout='column' ui-view></div>"
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
                templateUrl: "static/rushtracker/rush_detail.html",
                controller: 'RushDetailController as ctrl',
                resolve: {
                    promiseObj: function($http, $stateParams) {
                        return $http.get('/api/rush/' + $stateParams.id);
                    },
                    comments: function($http, $stateParams) {
                        return $http.get('/api/comments/?rush=' + $stateParams.id)
                    }
                }
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
            .state('brothers', {
                abstract: true,
                url: "/brothers",
                template: "<div ui-view></div>"
            })
            .state('brothers.list', {
                url: "/list",
                templateUrl: "static/chaptermanagement/user_index.html",
            })
            .state('recruitmentperiod' , {
                abstract: true,
                url: "/recruitmentperiod",
                template: "<div ui-view layout='column' flex></div>"
            })
            .state('recruitmentperiod.list', {
                url:"/list",
                templateUrl: "static/rushperiod/index.html",
                controller: "RecruitmentList as ctrl",
                resolve: {
                    promiseObj: function($http) {
                        return $http.get('/api/rushperiod/');
                    }
                }
            })
    });

    rushApp.controller('NavCtrl', function($scope, $location) {
        this.isActive = function(route) {
            return $location.path().includes(route);
        };
    });

})();
