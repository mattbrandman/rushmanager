(function(){

	var app = angular.module('RushApp', ['RushFactory', 'ui.bootstrap']);
	
	

	app.config(['$httpProvider', '$resourceProvider', function($httpProvider, $resourceProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
    $resourceProvider.defaults.stripTrailingSlashes = false;
	}]);

	app.controller('RushTableController', ['promiseObj', 'Rush', '$state', function(promiseObj, Rush, $state){
		var vm = this;
		this.page_size  = 100;
		var data = promiseObj.data;
		vm.rushes = data.results;
		vm.totalRushes = data.count;
		vm.perPage = vm.page_size;
		vm.page_size = 100;
		this.goDetail = function(id) {
			$state.go('rush.detail', {'id': id});
		} 
		this.reverse = false;
		var currentColumn = "first_name";
		this.active = "first_name";
		this.sort = function(column) {
			//if page size changes reset page
			if(vm.page_size != vm.perPage) {
				vm.paginationControl = 1;
			}
			//if no column is entered do nothing to reverse and column
			if(column == null) {

			}
			//if new column is picked then reset reverse filter
			else if(vm.active != column) {
				vm.reverse = false
			//if same column is clicked twice sort in reverse order
			} else {
				vm.reverse = !vm.reverse
			}
			if (column != null) {
				currentColumn = column;
				vm.paginationControl = 1;
			}
			var minusSign='';
			if (vm.reverse == true) {
				var minusSign = '-';
			}
			Rush.query({'ordering': minusSign + currentColumn,
						'page': vm.paginationControl,
						'search': vm.search,
						'page_size': vm.page_size}, function(data) {
				vm.rushes = data.results;
				vm.totalRushes = data.count;
				vm.perPage = vm.page_size;
			});
		}
	}]);

	app.controller('RushDetailController', ['promiseObj', function(promiseObj){
		this.rush = promiseObj.data;
		console.log(this.rush);
	}])

})();