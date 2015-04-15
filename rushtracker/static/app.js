(function(){
	var app = angular.module('rankingCreation', []);
	app.controller('RankingController', ['$scope', '$http', function( $scope, $http){
		$scope.listOfRushes = [{"first_name":"kmkll","last_name":"","id":1},];
			$http.get('/api/rush/').
			success(function(data, status, headers, config){
			//something funk with scopes and how data is formatted when returned
				$scope.listOfRushes = data;
			});
		}]);
})();