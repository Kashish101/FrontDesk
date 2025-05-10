# Simulated in-memory storage for pending requests
pending_requests = []

def add_pending_request(request):
    """Add a pending help request"""
    pending_requests.append(request)

def resolve_request(index, answer):
    """Resolve a pending request and store the answer"""
    if 0 <= index < len(pending_requests):
        pending_requests[index]['status'] = 'Resolved'
        pending_requests[index]['response'] = answer
        return True
    return False

def get_pending_requests():
    """Get all pending requests"""
    return pending_requests
