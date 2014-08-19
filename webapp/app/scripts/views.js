app.Views.Search = Marionette.ItemView.extend({
  template: JST['app/scripts/templates/search.html'],

  ui: {
    'inputAddress': 'input#address',
    'errorMessage': '#error-message'
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

    this.hideError();
    if ( searchString === '' ) {
      this.showError();
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

    this.hideError();
  },

  showError: function() {
    'use strict';

    this.ui.errorMessage.show();
  },

  hideError: function() {
    'use strict';

    this.ui.errorMessage.hide();
  }
});
