class CheckinController < ApplicationController
  def index
    @checkins = User.find(session[:user_id]).checkins.includes(:location).order('created_at DESC')
  end

  def new
    # TODO - read below
    #name = get location and use that as the name with random string
    # 38.733082	-109.592514 - arches national park utah

    name = "#{SecureRandom.urlsafe_base64}.#{params['file'].path.split('.').last}"
    FileUtils.mv(params['file'].path,"#{Rails.root.to_s}/app/assets/images/#{name}")
    Checkin.create(user_id: session[:user_id],lattitude: "38.733082", longitude: "-109.592514", location: "Arches National Park", image: name )
    render json: {
      suceess: true
    }
  end
end
