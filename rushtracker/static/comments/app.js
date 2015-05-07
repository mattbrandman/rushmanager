var app = angular.module('commentApp', ['ui.bootstrap', 'xeditable']);
	app.config(['$httpProvider', '$locationProvider', function($httpProvider, $locationProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
    $locationProvider.html5Mode(true);
}]);
	app.run(function(editableOptions) {
  	editableOptions.theme = 'bs3'; // bootstrap3 theme. Can be also 'bs2', 'default'
	});

	app.controller('CommentViewController', ['my_api', '$location', '$http', function(my_api, $location, $http) {
		
	var x = $location.path();
		x = x.split('/');
		x = x[2];

		this.all_comments;
		this.comment = {};
		this.comment.rush = x;
		this.my_comment_list = [];
		this.users = [];
		this.events = [];
		var _this = this;

		this.submit = function(comment) {
			var submitPromise = $http.post('/api/comments/', comment)
			submitPromise.success(function(data) {
				_this.all_comments.push(data);
			});
			this.comment = {};
			this.comment.rush = x;

		};
		this.isEqual = function(comment) {
			if(this.my_comment_list.indexOf(comment.id) >= 0) {
				return true;
			} else {
				return false;
			}
		};

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
			return $http.get('/api/comments/' + rush + '/get-comments/');
		};

		this.getUsers = function() {
			return $http.get('/api/users/');
		}

		this.getEvents = function() {
			return $http.get('/api/events/');
		}
	}]);