app.Controllers.MainController = Marionette.Controller.extend({
  index: function() {
    'use strict';
    this.searchController = new app.Controllers.Search();
    this.listenTo(this.searchController, 'location:found', this.locationFound);
    this.listenTo(this.searchController, 'location:found', this.locationNotFound);
  },

  locationFound: function(data) {
    'use strict';

    console.log(data);
  },

  locationNotFound: function(errorMsg) {
    'use strict';

    console.log(errorMsg);
  }
});

app.Controllers.Search = Marionette.Controller.extend({
  initialize: function() {
    'use strict';

    this.baseURL = app.settings.baseURL;
    this.searchView = new app.Views.Search();
    app.mainRegion.show(this.searchView);

    this.listenTo(this.searchView, 'call:search', this.search);
  },

  search: function(searchStr) {
    'use strict';

    if (searchStr === 'nearest') {
      this.searchByLocation();
    } else {
      this.searchByString(searchStr);
    }
  },

  searchByString: function(searchStr) {
    'use strict';

    $.get(this.searchURL(searchStr), function(data) {
      this.trigger('location:found', data);
    }).fail(function() {
      this.trigger('location:error', 'We could not find you.');
    });
  },

  searchByLocation: function() {
    'use strict';

    var locationFound,
        noGeolocation;

    locationFound = function(position) {
      $.get(this.locationURL(position), function(data) {
        this.trigger('location:found', data);
      });
    };

    noGeolocation = function() {
      this.trigger('location:error', 'Geolocation is not working.');
    };

    if ('geolocation' in navigator) {
      navigator.geolocation.getCurrentPosition(locationFound, noGeolocation);
    }
  },

  locationURL: function(position) {
    'use strict';

    var queryString = [
      'lat=' + position.coords.latitude,
      'lng=' + position.coords.longitude
    ].join('&');
    return this.baseURL + '/api/location?' + queryString;
  },

  searchURL: function(searchStr) {
    'use strict';

    return this.baseURL + '/api/search?q=' + searchStr;
  }
});
