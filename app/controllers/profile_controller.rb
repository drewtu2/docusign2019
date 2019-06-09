class ProfileController < ApplicationController
  def index
    @user = User.last
  end

  def update
    User.find(params[:id]).update(user_params.to_h)
    redirect_to profile_path
  end

  private
  def user_params
    params.require(:user).permit(:first_name, :last_name, :zip, :email, :phone_number, :username)
  end
end
