var app = angular.module('chapterManagement', []);
	app.config(['$httpProvider', function($httpProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
}]);

	app.controller('PageController', ['$http', function($http){	
		this.brothers = [];
		this.rush_committee = [];
		var _display = this;
		var getBrothers = $http.get('/api/users/');

		getBrothers.success(function(data) {
			_display.brothers = data;
		});

		this.ChangeCommitteeStatus = function(brother) {
			var id = brother.id;
			var url = '/api/users/' + id + '/';
			brother.id = 100;
			$http.patch(url, brother);
			brother.is_rush_committee = !brother.is_rush_committee;

		};

	}]);