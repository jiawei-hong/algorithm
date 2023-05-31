class EventEmitter {
    constructor() {
      this.events = {};
    }
  
    subscribe(event, f) {
      this.events[event] = this.events[event] ?? [];
      this.events[event].push(f);
        
      return {
          unsubscribe: () => {
            this.events[event] = this.events[event].filter(fn => fn !== f);
          }
      };
    }
  
    emit(event, args = []) {
      const hasEvent = event in this.events;
  
      if (!hasEvent) return [];
  
      return this.events[event].map(fn => fn(...args));
    }
  }