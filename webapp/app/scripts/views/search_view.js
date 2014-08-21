app.Views.Search = Marionette.ItemView.extend({
  template: JST['app/scripts/templates/search.html'],

  ui: {
    'inputAddress': 'input#address',
    'emptyError': '#empty-error',
    'notTexasError': 'not-texas-error'
  },

  events: {
    'submit #search-form': 'searchByAddress',
    'change #address': 'changeAddress',
    'click #find-me': 'findMe'
  },

  searchByAddress: function(event) {
    'use strict';
    event.preventDefault();

    var searchString = $.trim(this.ui.inputAddress.val());

    this.hideErrors();
    if ( searchString === '' ) {
      this.showEmptyError();
    } else {
      this.trigger('search:string', searchString);
    }
  },

  findMe: function(event) {
    'use strict';
    event.preventDefault();

    this.hideError();
    this.trigger('search:location');
  },

  changeAddress: function() {
    'use strict';

    this.hideErrors();
  },

  showEmptyError: function() {
    'use strict';

    this.ui.emptyError.show();
  },

  showNotTexasError: function() {
    'use strict';

    this.ui.notTexasError.show();
  },

  hideErrors: function() {
    'use strict';

    this.ui.emptyError.hide();
    this.ui.notTexasError.hide();
  }
});
