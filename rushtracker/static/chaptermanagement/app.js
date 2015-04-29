var app = angular.module('chapterManagement', ['ui.bootstrap']);
	app.config(['$httpProvider', function($httpProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
}]);
	app.value('Papa', Papa);

	app.controller('PageController', ['$http', '$modal', '$log', '$scope', 'Papa', function($http, $modal, $log, $scope, Papa){	
		this.brothers = [];
		this.rush_committee = [];
		var _display = this;
		var getBrothers = $http.get('/api/users/');
		$scope.items = ['item1', 'item2', 'item3']
		getBrothers.success(function(data) {
			_display.brothers = data;
		});

		this.ChangeCommitteeStatus = function(brother) {
			var id = brother.id;
			var url = '/api/users/' + id + '/change-rush-comm-status/';
			brother.is_rush_committee = !brother.is_rush_committee;
			$http.patch(url, brother);
		};


  		$scope.open = function (size) {

		    var modalInstance = $modal.open({
		      templateUrl: '/add_brother_modal.html',
		      controller: 'ModalInstanceCtrl',
		      controllerAs: 'ModalCtrl',
		      size: size,
		    });

		    modalInstance.result.then(function (data) {
		    	if(Array.isArray(data)) {
		    		data.forEach(function(data) {
		    			_display.brothers.push(data);
		    		});
		    	} else {
		      		_display.brothers.push(data);
		    	};
		    }, function () {
		      $log.info('Modal dismissed at: ' + new Date());
		    });
		};
	}]);



// Please note that $modalInstance represents a modal window (instance) dependency.
// It is not the same as the $modalservice used above.

	app.controller('ModalInstanceCtrl', function ($scope, $modalInstance, $http, Papa) {
	this.new_brother = {};
	var file = [];

	  this.uploadFile = function() {
	  	var x = document.getElementById("csvFile");
	  	Papa.parse(x.files[0], {
			complete: function(results) {
					file = results.data;
			},
			header:true,
		});
	  };


	  this.ok = function () {
		var promise = $http.post('/api/users/', this.new_brother);
		promise.success(function(data) {
			$modalInstance.close(data);
		});
	  };

	  this.okMany = function () {
	  	var promise = $http.post('/api/users/', file);
	  	promise.success(function(data) {
	  		$modalInstance.close(data);
	  	});
	  };

	  this.cancel = function () {
	    $modalInstance.dismiss('cancel');
	  };
	});

	app.directive('customOnChange', function() {
  		return {
    		restrict: 'A',
    		link: function (scope, element, attrs) {
      			var onChangeFunc = scope.$eval(attrs.customOnChange);
      			element.bind('change', onChangeFunc);
    		}
  		};
	});