# chapter-10
jacob, even

##  Description


###  Flowchart
```mermaid
graph TD;
  main --> class_retailltem
  main --> class_cashregister
  class_retailltem --> invintory_desplay
  class_retailltem --> Add_invintory
  class_retailltem --> save_invintory
  class_retailltem --> Exit_retailltem
  class_cashregister --> view_cart
  class_cashregister --> display_item
  class_cashregister --> buy_item
  class_cashregister --> empty_cart
  class_cashregister --> check_out
  class_cashregister --> Exit_cashregister
```

#### Function Diagrams

|  main   |               |    Jacob,even  |
| ------------------ | ------------- | ------------ |
|  no arguments   | Main calls class   |    returns nothing       |  
***
|   invintory_desplay  |               |    Jacob    |
| ------------------ | ------------- | ------------ |
|  accepts invintory  | shows all items in invintory |       returns invintory       |

***
|   Add_invintory  |               |    Jacob    |
| ------------------ | ------------- | ------------ |
|  accepts invintory  | adds item,number,and price to invintory  |     returns the new invintory     |

***
|  save_invintory   |               |   jacob     |
| ------------------ | ------------- | ------------ |
|  accept invintory   |  saves invintory  |      returns new_inventory        |
***
|  Exit_retailltem   |               |  jacob      |
| ------------------ | ------------- | ------------ |
|  accepts nothing   |  returns to main  |  returns nothing   |       
***
|  view_cart   |               |    even    |
| ------------------ | ------------- | ------------ |
|     |    |              |
***
|  display_item   |               |     even   |
| ------------------ | ------------- | ------------ |
|       |              |
***
|   buy_item  |               |     even   |
| ------------------ | ------------- | ------------ |
|       |              |
***
|    empty_cart |               |     even   |
| ------------------ | ------------- | ------------ |
|       |              |
***
|  check_out   |               |     even   |
| ------------------ | ------------- | ------------ |
|       |              |
***
|  Exit_cashregister   |               |     even   |
| ------------------ | ------------- | ------------ |
|       |              |
***
