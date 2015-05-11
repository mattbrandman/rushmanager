(function() {
var app = angular.module('commentApp', ['ui.bootstrap', 'xeditable', 'ui.select', 'ngSanitize']);
	app.config(['$httpProvider', '$locationProvider', function($httpProvider, $locationProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'x-CSRFToken';
    $locationProvider.html5Mode(true);
}]);
	//TODO: maybe I should load events and user 
	//in the django template or all at once 
	//so that I don't have to hit the database
	//a bunch of times
	app.run(function(editableOptions) {
  	editableOptions.theme = 'bs3'; // bootstrap3 theme. Can be also 'bs2', 'default'
	});

	app.controller('CommentViewController', ['my_api', '$location', '$http', function(my_api, $location, $http) {
		var _this = this; 
		
		var rushId = $location.path();
		rushId = rushId.split('/');
		rushId = rushId[2];

		this.picture;
		my_api.getRush(rushId).success(function(data) {
			_this.picture = data.picture;
		});

		this.is_admin = _currentUser.is_admin;
		this.all_comments = [];
		this.comment = {};
		this.comment.user = {};
		this.comment.rush = rushId;
		this.my_comment_list = [];
		this.users = [];
		this.events = [];


		this.submit = function(comment) {
			var submitPromise = $http.post('/api/comments/', comment)
			submitPromise.success(function(data) {
				_this.all_comments.push(data);
				_this.my_comment_list.push(data.id)
				_this.comment.comment = "";
			});

		};
		this.isEqual = function(comment) {
			if(this.my_comment_list.indexOf(comment.id) >= 0) {
				return true;
			} else {
				return false;
			}
		};

		this.update = function(comment) {
			var toSend = {'comment': comment.comment};
			$http.patch('/api/comments/' + comment.id + '/', toSend);
		}

		var promise = my_api.getComments(rushId);
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
			_this.comment.user = _currentUser.user;
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
		};

		this.getEvents = function() {
			return $http.get('/api/events/');
		};

		this.getRush = function(id) {
			return $http.get('/api/rush/' + id + '/');
		};
	}]);


})();