app.Views.AVContextRow = Marionette.ItemView.extend({
  template: JST['app/scripts/templates/av_context_row.html'],
  tagName: 'tr'
});

_.extend(app.Views.AVContextRow.prototype, app.Mixins.Helpers);
