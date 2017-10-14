import block
import Chain

chain = Chain.Blockchain()

first = block.Block('first')
second = block.Block('second')
third = block.Block('third')

chain.add_block(first)
chain.add_block(second)
chain.add_block(third)

first.update_data('so broke')

print(chain.broken)  # True

#chain.repair()

print(chain.broken)  # False