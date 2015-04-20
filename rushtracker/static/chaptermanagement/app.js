var app = angular.module('chapterManagement', ['ui.bootstrap']);
	app.config(['$httpProvider', function($httpProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
}]);

	app.controller('PageController', ['$http', '$modal', '$log', '$scope', function($http, $modal, $log, $scope){	
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
			var url = '/api/users/' + id + '/';
			brother.is_rush_committee = !brother.is_rush_committee;
			$http.patch(url, brother);
		};


  		$scope.open = function (size) {

		    var modalInstance = $modal.open({
		      templateUrl: 'add_brother_modal',
		      controller: 'ModalInstanceCtrl',
		      controllerAs: 'ModalCtrl',
		      size: size,
		    });

		    modalInstance.result.then(function (brother) {
		      _display.brothers.push(brother);
		    }, function () {
		      $log.info('Modal dismissed at: ' + new Date());
		    });
		};
	}]);



// Please note that $modalInstance represents a modal window (instance) dependency.
// It is not the same as the $modalservice used above.

	app.controller('ModalInstanceCtrl', function ($scope, $modalInstance, $http) {
	this.new_brother = {};
	  this.ok = function () {
	    var promise = $http.post('/api/users/', this.new_brother);
	    promise.success(function(data) {
	    	$modalInstance.close(data);
	    });
	  };

	  this.cancel = function () {
	    $modalInstance.dismiss('cancel');
	  };
	});