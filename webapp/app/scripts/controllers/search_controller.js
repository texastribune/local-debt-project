app.Controllers.Search = Marionette.Controller.extend({
  initialize: function() {
    'use strict';

    this.baseURL = app.Settings.baseURL;
    this.searchView = new app.Views.Search();
    app.searchRegion.show(this.searchView);

    this.listenTo(this.searchView, 'search:string', this.searchByString);
    this.listenTo(this.searchView, 'search:location', this.searchByLocation);
  },

  searchByString: function(searchStr) {
    'use strict';

    var self = this;

    $.ajax({
      url: this.searchURL(searchStr),
      dataType: 'jsonp',
      jsonp: 'callback',
      jsonpCallback: 'jsonpCallback',
      success: function(data){

        self.displaySearchString(data).trigger('location:found', data);
      }
    }).fail(function() {
      this.searchView.showNotTexasError();
    });
  },

  displaySearchString: function(data) {
    'use strict';
    this.searchMessageView = new app.Views.SearchMessage({
      model: new app.Models.SearchString(data.meta)
    });
    app.searchStringRegion.show(this.searchMessageView);

    return this;
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
