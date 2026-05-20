// fn main() {
//     println!("Hello, world!");
// }
fn main() {
	let mylist = [ "One", "Two", "Three" ];
	for item in &mylist {
		println!("{}", item);
	}
}
