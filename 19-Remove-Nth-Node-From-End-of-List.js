/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} n
 * @return {ListNode}
 */
var removeNthFromEnd = function(head, n) {
    if (head == null || head.next == null) return null
    
    let cur = head
    let counter = 0

    while(cur){
        counter++
        cur = cur.next
    }

    let indx = counter - n 
    cur = head
    let pre = head
    while(indx > 0){
        pre = cur
        cur = cur.next
        indx--
    }
    if (cur == head){
        head = cur.next
    } else { 
        pre.next = cur.next
    }

    return head

};