class ApplicationController < ActionController::Base
  before_action :set_user
  skip_before_action :verify_authenticity_token

  def set_user
    return if session[:user_id].present?
    user = User.last
    session[:user_id] = user.id
    %I(username first_name last_name email zip).each do |attr|
      session[attr] = user.send(attr)
    end
  end
end
