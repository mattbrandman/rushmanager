(function(){

	var app = angular.module('RushApp', ['RushFactory', 'ui.bootstrap']);
	
	

	app.config(['$httpProvider', function($httpProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
	}]);

	app.controller('RushTableController', ['Rush', function(Rush){
		var vm = this;
		Rush.query(function(data) {
			vm.rushes = data.results;
			vm.totalRushes = data.count;
			vm.perPage = 10;
		});
		this.reverse = false;
		var currentColumn = null;
		this.sort = function(column) {
			if (this.column == null && currentColumn != null) {
				paginationControl = 1;
			} else {
				currentColumn = column;
				paginationControl = 1;
			}
			var minusSign='';
			if (vm.reverse == true) {
				var minusSign = '-';
			}
			Rush.query({'ordering': minusSign + currentColumn,
						'page': vm.paginationControl}, function(data) {
				vm.rushes = data.results;
				console.log(vm.rushes);
			});
		}
	}]);

})();