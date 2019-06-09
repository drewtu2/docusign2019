Rails.application.routes.draw do
  root to: 'profile#index'
  get '/profile', to: 'profile#index'
  resources :profile
  get '/parks', to: 'parks#index'
  get '/checkin', to: 'checkin#index'
  get '/wallet', to: 'wallets#index'
  get '/advocacy', to: 'advocacy#index'
  post '/profile/:id', to: 'profile#update'
  post '/checkin', to: 'checkin#new'
  resources :advocacy
end
