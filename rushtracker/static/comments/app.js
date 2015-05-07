var app = angular.module('commentApp', ['ui.bootstrap', 'xeditable']);
	app.config(['$httpProvider', '$locationProvider', function($httpProvider, $locationProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
    $locationProvider.html5Mode(true);
}]);
	app.run(function(editableOptions) {
  	editableOptions.theme = 'bs3'; // bootstrap3 theme. Can be also 'bs2', 'default'
	});

	app.controller('CommentViewController', ['my_api', '$location', function(my_api, $location) {
		this.all_comments;
		this.my_comment_list = [];
		this.users = [];
		this.events = [];



		this.isEqual = function(comment) {
			if(this.my_comment_list.indexOf(comment.id) >= 0) {
				return true;
			} else {
				return false;
			}
		};
		var x = $location.path();
		x = x.split('/');
		x = x[2];
		var _this = this;

		var promise = my_api.getComments(x);
		promise.success(function(data) {
			_this.all_comments = data['all_comments'];
			var my_comments = data['my_comments'];
			my_comments.forEach(function(c) {
				_this.my_comment_list.push(c.id);
			});
		});

		var userPromise = my_api.getUsers();
		userPromise.success(function(data) {
			_this.users = data;
		});

		var eventPromise = my_api.getEvents();
		eventPromise.success(function(data) {
			_this.events = data;
		})
	}]);

	app.service('my_api', ['$http', function($http) {
		this.getComments = function(rush) {
			return $http.get('/api/comments/' + rush + '/get-comments/').
			success(function(data, status, headers, config){
				return data;
			//something funk with scopes and how data is formatted when returned
		});
		};

		this.getUsers = function() {
			return $http.get('/api/users/');
		}

		this.getEvents = function() {
			return $http.get('/api/events/');
		}
	}]);