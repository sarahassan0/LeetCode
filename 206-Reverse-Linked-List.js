/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var reverseList = function(head) {
    if(head === null) return head;

    stack = []
    while(head !== null){
        stack.push(head);
        head = head.next;
    }

    head = stack.pop()
    node = head
    while (stack.length ){ 
        node.next = stack.pop()
        node = node.next
    }
    node.next = null

    return head
};