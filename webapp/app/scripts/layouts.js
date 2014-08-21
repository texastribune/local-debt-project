app.Layouts.EntityLayout = Backbone.Marionette.LayoutView.extend({
  template: JST['app/scripts/templates/entity_layout.html'],
  className: 'debt-result',

  regions: {
    'debtBox': '.debt-box',
    'debtContext': '.debt-context',
    'debtByPop': '.by-pop',
    'debtByAV': '.by-av'
  },
});
