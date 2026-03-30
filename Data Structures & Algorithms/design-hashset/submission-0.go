type MyHashSet struct {
	Set []bool
}

func Constructor() MyHashSet {
	set := make([]bool, 1_000_001)
	return MyHashSet{Set: set}
}

func (this *MyHashSet) Add(key int) {
	this.Set[key] = true
}

func (this *MyHashSet) Remove(key int) {
	this.Set[key] = false
}

func (this *MyHashSet) Contains(key int) bool {
	return this.Set[key]
}

/**
 * Your MyHashSet object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Add(key);
 * obj.Remove(key);
 * param_3 := obj.Contains(key);
 */
 