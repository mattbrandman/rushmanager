(function() {
var app = angular.module('chapterManagement', ['ui.bootstrap']);
	app.config(['$httpProvider', function($httpProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
}]);

	app.controller('PageController', ['$http', '$uibModal', '$log', '$scope', function($http, $uibModal, $log, $scope){	
		this.brothers = [];
		this.rush_committee = [];
		var _display = this;
		var getBrothers = $http.get('/api/users/');
		getBrothers.success(function(data) {
			_display.brothers = data;
		});

		this.ChangeCommitteeStatus = function(brother) {
			var id = brother.id;
			var url = '/api/users/' + id + '/change-rush-comm-status/';
			brother.is_rush_committee = !brother.is_rush_committee;
			$http.patch(url, brother);
		};

		this.ResetPassword = function(brother) {
			var id = brother.id;
			var promise = $http.get('/api/users/' + id + '/reset-to-default-password/');
			promise.success(function(data) {
				brother.reset = true;
				alert(data.message);
			});
		}


  		$scope.open = function (size) {

		    var modalInstance = $uibModal.open({
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

	app.controller('ModalInstanceCtrl', function ($scope, $modalInstance, $http) {
	this.new_brother = {};
	var file = [];



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
})();


