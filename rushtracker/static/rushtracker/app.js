(function() {

    var app = angular.module('RushApp', ['RushFactory', 'ngAnimate', 'ngFileUpload', 'ngImgCrop']);


    app.config(['$httpProvider', '$resourceProvider', function($httpProvider, $resourceProvider) {
        $httpProvider.defaults.xsrfCookieName = 'csrftoken';
        $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
        $resourceProvider.defaults.stripTrailingSlashes = false;
    }]);

    app.controller('RushTableController', ['promiseObj', 'brotherPromiseObj', 'Rush', '$state', '$http', 'Upload', '$mdDialog', function(promiseObj, brotherPromiseObj, Rush, $state, $http, Upload, $mdDialog) {
        this.selected = [];
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
                    headers: {
                        'Content-Type': 'image/png'
                    }
                }).then(function(data) {
                    Rush.patch({
                        rushId: rush.id
                    }, {
                        'picture': customUrl
                    });
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

        this.newRushDialog = function($event) {
            $mdDialog.show({
                targetEvent: $event,
                templateUrl: '/static/rushtracker/create_rush.html',
                controllerAs: 'newRushController as ctrl',
                resolve: {
                    promiseObj: function() { 
                        return $http.get('/api/rushperiod/');s
                    }
                }
            })
        }


    }]);
    app.controller('newRushController', ['$mdDialog', 'promiseObj', function($mdDialog, promiseObj){
        this.getMatches = function(searchText) {
            
        }
    }])
    app.controller('RushDetailController', ['promiseObj', 'comments', '$http', function(promiseObj, comments, $http) {
        _this = this;
        this.rush = promiseObj.data;
        this.comments = comments.data;

        this.submitComment = function() {
            var promise = $http.post('/api/comments/', {
                'comment': this.newComment,
                'rush': this.rush.id,
                'user': _currentUser.user
            });
            promise.then(function(data) {
                _this.newComment = "";
            });
        }
    }]);

})();
