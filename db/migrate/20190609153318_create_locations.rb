class CreateLocations < ActiveRecord::Migration[5.2]
  def change
    create_table :locations do |t|
      t.string :name
      t.string :state
      t.string :longitude
      t.string :lattitude
      t.timestamps
    end
  end
end
