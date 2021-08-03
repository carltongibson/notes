# Async Let in Swift

Swift’s `async let` is nice. It lets you await multiple asynchronous calls at once.

```swift
func loadImages() {
    Task {
        async let firstImage = await loadImage(index: 1)
        async let secondImage = await loadImage(index: 2)
        async let thirdImage = await loadImage(index: 3)
        let images = await [firstImage, secondImage, thirdImage]
    }
}
```

Much like `asyncio.gather()`:

```python
L = await asyncio.gather(
   factorial("A", 2),
   factorial("B", 3),
   factorial("C", 4),
)
```

* Antoine van der Lee on [Async let explained: call async functions in parallel](https://www.avanderlee.com/swift/async-let-asynchronous-functions-in-parallel/)
* Python docs on [Asyncio: Coroutines and Tasks](https://docs.python.org/3/library/asyncio-task.html#running-tasks-concurrently)