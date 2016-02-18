(function() {


    var app = angular.module('recruitmentPeriod', []);

    app.config(['$httpProvider', function($httpProvider) {
        $httpProvider.defaults.xsrfCookieName = 'csrftoken';
        $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
    }]);

    app.controller('RecruitmentList', ['promiseObj', '$mdDialog', function(promiseObj, $mdDialog) {
        var _this = this;
        this.recPerList = promiseObj.data;


        this.newRushPeriodDialog = function($event) {
            $mdDialog.show({
                targetEvent: $event,
                templateUrl: '/static/rushperiod/create_rushperiod.html',
                controller: "RushPeriodDialogController",
                controllerAs: "ctrl"          
                });
        };
    }]);
    
    app.controller('RushPeriodDialogController', ['$http', function($http){
        var _this = this;
        this.newRecruitmentPeriod = {};
        this.save = function() {
            console.log(this.newRecruitmentPeriod.start_date.dateString);
            $http.post('/api/rushperiod/', _this.newRecruitmentPeriod);
        };
    }]);



})();
