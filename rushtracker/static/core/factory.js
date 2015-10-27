(function() {
    var app = angular.module('RushFactory', ['ngResource']);
    app.factory('Rush', ['$resource', function($resource) {
        return $resource('/api/rush/:rushId/', null, {
        	'update': {
        		method: 'PUT'
        	},
        	'query': {
        		isArray:false
        	}

        });
    }]);
})();
