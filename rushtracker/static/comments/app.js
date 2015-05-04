var app = angular.module('commentApp', ['ui.bootstrap', 'xeditable']);
	app.config(['$httpProvider', '$locationProvider', function($httpProvider, $locationProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
    $locationProvider.html5Mode(true);
}]);
	app.run(function(editableOptions) {
  	editableOptions.theme = 'bs3'; // bootstrap3 theme. Can be also 'bs2', 'default'
	});

	app.controller('CommentViewController', ['getComments', '$location', function(getComments, $location) {
		this.all_comments;
		this.my_comment_list = [];

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
		var promise = getComments.getComments(x);
		promise.success(function(data) {
			_this.all_comments = data['all_comments'];
			var my_comments = data['my_comments'];
			my_comments.forEach(function(c) {
				_this.my_comment_list.push(c.id);
			});
		});
	}]);

	app.service('getComments', ['$http', function($http) {
		this.getComments = function(rush) {
			return $http.get('/api/comments/' + rush + '/get-comments/').
			success(function(data, status, headers, config){
				return data;
			//something funk with scopes and how data is formatted when returned
		});
		};
	}]);