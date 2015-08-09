(function(){
	'use strict';
	angular
		.module('app', ['ngMaterial'])
		.config(function ($mdThemingProvider) {
            $mdThemingProvider
                .theme('default')
                .primaryPalette('green')
                .accentPalette('orange');
        })
        .config(['$mdIconProvider', function ($mdIconProvider) {
            $mdIconProvider
                .iconSet('action', '/static/web/icons/action.svg', 24)
                .iconSet('navigation', '/static/web/icons/navigation.svg', 24);
                /*
                .iconSet('action', 'svg/action-icons.svg')
                .iconSet('device', 'svg/device-icons.svg')
                .iconSet('content', 'svg/content-icons.svg')
                .iconSet('alert', 'svg/alert-icons.svg')
               .iconSet('image', 'svg/image-icons.svg');*/
        }])
        .controller('AppCtrl', ['$scope', '$mdSidenav', function ($scope, $mdSidenav) {
        	$scope.toggleSidenav = function (menuId) {
        		$mdSidenav(menuId).toggle();
        	};
            $scope.page_active = 'home';
            $scope.setPageActive = function(index){
                $scope.page_active = $scope.menu[index].title;
            }
            $scope.header = 'Cooks To Go';
            $scope.menu = [
            {
                icon: 'action:home',
                title: 'home'
            },
            {
                icon: 'action:home',
                title: 'recipes'
            },
            {
                icon: 'action:home',
                title: 'ingredients'
            },
            {
                icon: 'action:shopping_basket',
                title: 'virtual basket'
            },
            {
                icon: 'action:settings',
                title: 'settings'
            },
            ];
        }]);
}());