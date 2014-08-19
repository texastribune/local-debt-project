app.Controllers.Main = Marionette.Controller.extend({
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
