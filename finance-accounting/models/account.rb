class Account < ApplicationRecord
  validates :name, presence: true, uniqueness: true
  validates :account_type, presence: true

  has_many :transactions

  enum account_type: { asset: 0, liability: 1, equity: 2, revenue: 3, expense: 4 }
end
