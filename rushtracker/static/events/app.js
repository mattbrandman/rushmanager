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
				var temp = []
				var i;
				for (i = 0; i < this.event.attendance.length; i ++) {
					temp.push(this.event.attendance[i].id);
				}
				//this has to be set first or apply won't be called on
				//the ui-select because if the first bind is not to a list then 
				//it will bind to its own internal model, so selected will still be 
				//available for the model but what previous selects will not be stored
				//or referenced
				this.event.attendance = [];
				console.log(this.event.attendance);
				this.updateAttendance = function(updateList) {
					this.response = $http.patch('/api/events/' + this.event.id + '/', {attendance: updateList});
					this.response.success(function(data) {
						alert('Update Successfully')
					});
				};

				var promiseRush = $http.get('/api/rush/');
				promiseRush.success(function(data) {
					_this.testList = data;
					_this.event.attendance = temp;
				});
				console.log('me');
				console.log(this.event.attendance);
			},
			controllerAs: 'ctrl',
			bindToController: true,
			require: 'ngModel',
			restrict: 'E',
			templateUrl: '/static/directives/attendanceDropDown.html',
		};
	});

})();