(function() {

    var app = angular.module('RushApp', ['RushFactory', 'ngAnimate', 'ngFileUpload', 'ngImgCrop']);


    app.config(['$httpProvider', '$resourceProvider', function($httpProvider, $resourceProvider) {
        $httpProvider.defaults.xsrfCookieName = 'csrftoken';
        $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
        $resourceProvider.defaults.stripTrailingSlashes = false;
    }]);

    app.controller('RushTableController', ['promiseObj', 'brotherPromiseObj', 'Rush', '$state', '$uibModal', '$http', 'Upload', function(promiseObj, brotherPromiseObj, Rush, $state, $uibModal, $http, Upload) {
        var vm = this;
        this.brothers = brotherPromiseObj.data;
        this.page_size = 100;
        vm.pickingPicture = false;
        var data = promiseObj.data;
        vm.rushes = data.results;
        vm.totalRushes = data.count;
        vm.perPage = vm.page_size;
        vm.page_size = 100;
        this.goDetail = function(id) {
            $state.go('rush.detail', {
                'id': id
            });
        }
        this.upload = function(file, rush) {
            var myUrl = $http.get('/api/rush/0/signs3/').then(function(data) {
                var customUrl = data.data.myUrl;
                $http({
                    url: data.data.url,
                    method: 'PUT',
                    data: Upload.dataUrltoBlob(file),
                    headers: {'Content-Type': 'image/png'}
                }).then(function(data) {
                    Rush.patch({rushId:  rush.id}, {'picture': customUrl});
                    rush.picture = customUrl;
                    rush.pickingPicture = false;
                });
            });
        }
        this.getContact = function(input) {
            var index = vm.brothers.map(function(x) {
                return x.id;
            }).indexOf(input);
            return vm.brothers[index];
        };
        this.reverse = false;
        var currentColumn = "first_name";
        this.active = "first_name";
        this.sort = function(column) {
            //if page size changes reset page
            if (vm.page_size != vm.perPage) {
                vm.paginationControl = 1;
            }
            //if no column is entered do nothing to reverse and column
            if (column == null) {

            }
            //if new column is picked then reset reverse filter
            else if (vm.active != column) {
                vm.reverse = false
                    //if same column is clicked twice sort in reverse order
            } else {
                vm.reverse = !vm.reverse
            }
            if (column != null) {
                currentColumn = column;
                vm.paginationControl = 1;
            }
            var minusSign = '';
            if (vm.reverse == true) {
                var minusSign = '-';
            }
            Rush.query({
                'ordering': minusSign + currentColumn,
                'page': vm.paginationControl,
                'search': vm.search,
                'page_size': vm.page_size
            }, function(data) {
                vm.rushes = data.results;
                vm.totalRushes = data.count;
                vm.perPage = vm.page_size;
            });
        }

        this.open = function() {
            var modalInstance = $uibModal.open({
                animation: true,
                templateUrl: '/static/rushtracker/create_rush.html',
                controller: 'NewRushModalInstanceCtrl',
                controllerAs: 'ctrl',
                resolve: {
                    brothers: function() {
                        return $http.get('/api/users/');
                    },
                    rush_periods: function() {
                        return $http.get('/api/rushperiod/')
                    }
                }
            });
            modalInstance.result.then(function(data) {
                vm.rushes.push(data);
                vm.totalRushes += 1;
            });

        };

        this.update = function(id) {
            var modalInstance = $uibModal.open({
                templateUrl: '/static/rushtracker/create_rush.html',
                controller: 'NewRushModalInstanceCtrl',
                controllerAs: 'ctrl',
                resolve: {
                    brothers: function() {
                        return $http.get('/api/users/');
                    },
                    rush_periods: function() {
                        return $http.get('/api/rushperiod/');
                    },
                    currentRush: function() {
                        return $http.get('/api/rush/' + id + '/?format=json');
                    }
                }
            });
            modalInstance.result.then(function(data) {
                vm.sort();
            });
        }

    }]);

    app.controller('RushDetailController', ['promiseObj', function(promiseObj) {
        this.rush = promiseObj.data;
    }]);

    app.controller('NewRushModalInstanceCtrl', ['$uibModalInstance', 'brothers', 'Rush', 'rush_periods', 'currentRush', function($uibModalInstance, brothers, Rush, rush_periods, currentRush) {
        var updating = false;
        if (currentRush == null) {
            console.log(null);
        } else {
            updating = true;
            this.rush = currentRush.data;
        }
        this.brothers = brothers.data
        this.rushPeriods = rush_periods.data
        this.rush;
        this.save = function() {
            if (updating == true) {
                Rush.update({
                    'rushId': this.rush.id
                }, this.rush);
                $uibModalInstance.close()
            } else {
                Rush.save(this.rush, function(data) {
                    $uibModalInstance.close(data);
                });
            }
        }
        this.cancel = function() {
            $uibModalInstance.dismiss('cancel');
        }
    }]).value('currentRush', null);

})();
