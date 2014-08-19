app.Controllers.MainController = Marionette.Controller.extend({
  index: function() {
    'use strict';
    this.searchController = new app.Controllers.Search();
  }
});

app.Controllers.Search = Marionette.Controller.extend({
  initialize: function() {
    'use strict';
    this.searchView = new app.Views.Search();
    app.mainRegion.show(this.searchView);

    this.listenTo(this.searchView, 'call:search', this.search);
  },

  search: function() {
    'use strict';
  }
});
