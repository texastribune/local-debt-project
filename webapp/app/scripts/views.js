app.Views.Search = Marionette.ItemView.extend({
  template: JST['app/scripts/templates/search.html'],

  ui: {
    'inputAddress': 'input#address'
  },

  events: {
    'submit #search-form': 'searchByAddress',
    'click #find-me': 'findMe'
  },

  searchByAddress: function(event) {
    'use strict';
    event.preventDefault();

    var searchString = $.trim(this.ui.inputAddress.val());

    if ( searchString === '' ) {
      // Show error messages
    } else {
      this.trigger('call:search', searchString);
    }
  },

  findMe: function(event) {
    'use strict';
    event.preventDefault();

    this.trigger('call:searh', 'nearest');
  }
});
