(function() {
var app = angular.module('eventManagement', ['ui.bootstrap', 'ui.select', 'ngSanitize']);
	app.config(['$httpProvider', function($httpProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
}]);

	app.controller('EventController', ['$http', '$scope', function($http, $scope) {
		var _this = this;
		this.testList = [];
		this.rushList = [];
		var promise = $http.get('/api/events/');


		promise.success(function(data) {
			_this.rushList = data;
			console.log(data);
		});


		var promiseRush = $http.get('/api/rush/');
		promiseRush.success(function(data) {
			_this.testList = data;
		});
	}]);

	//TODO: move all lists into services 
	app.directive('rushAttendance', function(){
		return {
			scope: {
				event: '=ngModel'
			},
			controller: function($http, $scope) {
				var _this = this;
				this.testList = [];
				this.rushList = [];
				var temp = $scope.event.attendance.map(function(obj) {
					return obj.id
				});
				$scope.event.attendance = temp;
				this.updateAttendance = function(updateList) {
					this.response = $http.patch('/api/events/' + $scope.event.id + '/', {attendance: updateList});
					this.response.success(function(data) {
						alert('Update Successfully')
					});
				};


				var promise = $http.get('/api/events/');
				promise.success(function(data) {
					_this.rushList = data;
				});


				var promiseRush = $http.get('/api/rush/');
				promiseRush.success(function(data) {
					_this.testList = data;
				});
			},
			controllerAs: 'ctrl',
			require: 'ngModel',
			restrict: 'E',
			templateUrl: '/static/directives/attendanceDropDown.html',
		};
	});

})();