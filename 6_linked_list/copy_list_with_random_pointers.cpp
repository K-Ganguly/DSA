// LeetCode Link: https://leetcode.com/problems/copy-list-with-random-pointer/
/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;

    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};
*/

class Solution
{
public:
    Node *copyRandomList(Node *head)
    {
        // Create a map to store the mapping from original nodes to their corresponding copies.
        unordered_map<Node *, Node *> nodes;

        // First pass: Create new nodes, copying the values from the original list.
        Node *curr = head;
        while (curr)
        {
            nodes[curr] = new Node(curr->val);
            curr = curr->next;
        }

        // Second pass: Connect the new nodes' 'next' and 'random' pointers.
        curr = head;
        while (curr)
        {
            // Get the corresponding new node from the map.
            Node *newNode = nodes[curr];

            // Connect the 'next' pointer of the new node.
            newNode->next = nodes[curr->next];

            // Connect the 'random' pointer of the new node.
            newNode->random = nodes[curr->random;

            curr = curr->next;
        }

        // Return the head of the new list, which is the copy of the original list.
        return nodes[head];
    }
};
