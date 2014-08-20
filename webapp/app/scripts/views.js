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

    this.hideError();
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

app.Views.Entity = Marionette.ItemView.extend({
  template: JST['app/scripts/templates/entity.html'],

  templateHelpers: function() {
    'use strict';

    var isACounty = this.model.get('issuerType') === 'county',
        isAIDS = this.model.get('issuerType') === 'isd',
        isACity = this.model.get('issuerType') === 'city';

    return {
      'isACounty': isACounty,
      'isAIDS': isAIDS,
      'isACity': isACity
    };
  },

  onRender: function() {
    'use strict';

    this.$el.addClass(this.model.get('issuerType'));
  }
});

app.Views.Entities = Marionette.CollectionView.extend({
  childView: app.Views.Entity,
  className: 'prose'
});
