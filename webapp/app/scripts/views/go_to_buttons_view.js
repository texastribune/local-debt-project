app.Views.GoToButtons = Marionette.CompositeView.extend({
  template: JST['app/scripts/templates/go_to_buttons.html'],
  childView: app.Views.GoToButton
});
